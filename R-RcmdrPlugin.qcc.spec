%global packname  RcmdrPlugin.qcc
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.6
Release:          1%{?dist}
Summary:          Rcmdr qcc Plug-In

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-6.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-tcltk R-qcc 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-tcltk R-qcc 

%description
This package provides an Rcmdr "plug-in" based on the qcc package, and it
provides an integration between the user and the tools of SPC.

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
%doc %{rlibdir}/RcmdrPlugin.qcc/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.qcc/html
%{rlibdir}/RcmdrPlugin.qcc/INDEX
%{rlibdir}/RcmdrPlugin.qcc/Meta
%{rlibdir}/RcmdrPlugin.qcc/R
%{rlibdir}/RcmdrPlugin.qcc/help
%{rlibdir}/RcmdrPlugin.qcc/etc

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.6-1
- initial package for Fedora