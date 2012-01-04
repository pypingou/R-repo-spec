%global packname  RcmdrPlugin.SLC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.1
Release:          1%{?dist}
Summary:          SLC Rcmdr Plug-in

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-SLC 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-SLC 

%description
This package provides a GUI for the SLC package, it is written as an Rcmdr

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
%doc %{rlibdir}/RcmdrPlugin.SLC/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.SLC/html
%{rlibdir}/RcmdrPlugin.SLC/R
%{rlibdir}/RcmdrPlugin.SLC/etc
%{rlibdir}/RcmdrPlugin.SLC/help
%{rlibdir}/RcmdrPlugin.SLC/INDEX
%{rlibdir}/RcmdrPlugin.SLC/Meta

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1-1
- initial package for Fedora