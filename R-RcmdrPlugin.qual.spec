%global packname  RcmdrPlugin.qual
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.2.0
Release:          1%{?dist}
Summary:          Rcmdr plugin for quality control course

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-qcc 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-qcc 

%description
This package provides an Rcmdr "plug-in" based on the Quality control
class Stat 4300

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
%doc %{rlibdir}/RcmdrPlugin.qual/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.qual/html
%{rlibdir}/RcmdrPlugin.qual/Meta
%{rlibdir}/RcmdrPlugin.qual/help
%{rlibdir}/RcmdrPlugin.qual/INDEX
%{rlibdir}/RcmdrPlugin.qual/etc
%{rlibdir}/RcmdrPlugin.qual/R

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.2.0-1
- initial package for Fedora