%global packname  tm.plugin.dc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.7
Release:          1%{?dist}
Summary:          Text Mining Distributed Corpus Plug-In

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-tm 
Requires:         R-slam 

BuildRequires:    R-devel tex(latex) R-tm
BuildRequires:    R-slam 


%description
A plug-in for the text mining framework tm to support text mining in a
distributed way. The package provides a convinient interface for handling
(distributed) storage.

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7-1
- initial package for Fedora