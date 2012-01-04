%global packname  RcmdrPlugin.orloca
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          2.1
Release:          1%{?dist}
Summary:          orloca Rcmdr Plug-in

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-orloca R-orloca.es 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-orloca R-orloca.es 

%description
This package provides a GUI for the orloca package, it is developed as an
Rcmdr plug-in.

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
%doc %{rlibdir}/RcmdrPlugin.orloca/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.orloca/html
%{rlibdir}/RcmdrPlugin.orloca/help
%{rlibdir}/RcmdrPlugin.orloca/INDEX
%{rlibdir}/RcmdrPlugin.orloca/R
%{rlibdir}/RcmdrPlugin.orloca/etc
%{rlibdir}/RcmdrPlugin.orloca/Meta
%{rlibdir}/RcmdrPlugin.orloca/po

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1-1
- initial package for Fedora