%global packname  genArise
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.30.0
Release:          1%{?dist}
Summary:          Microarray Analysis tool

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-locfit R-tkrplot R-methods 
Requires:         R-graphics R-grDevices R-methods R-stats R-tcltk R-utils R-xtable 

BuildRequires:    R-devel tex(latex) R-locfit R-tkrplot R-methods
BuildRequires:    R-graphics R-grDevices R-methods R-stats R-tcltk R-utils R-xtable 


%description
genArise is an easy to use tool for dual color microarray data. Its GUI-Tk
based environment let any non-experienced user performs a basic, but not
simple, data analysis just following a wizard. In addition it provides
some tools for the developer.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%changelog
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.30.0-1
- initial package for Fedora