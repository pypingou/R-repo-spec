%global packname  RcmdrPlugin.SurvivalT
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.7
Release:          1%{?dist}
Summary:          Rcmdr Survival Plug-In

Group:            Applications/Engineering 
License:          GPL version 2 or newer
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-Rcmdr R-survival 

BuildRequires:    R-devel tex(latex) R-Rcmdr R-survival 

%description
This package provides an Rcmdr "plug-in" based on the survival package for
easier student access to survival analysis.

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
%doc %{rlibdir}/RcmdrPlugin.SurvivalT/DESCRIPTION
%doc %{rlibdir}/RcmdrPlugin.SurvivalT/html
%{rlibdir}/RcmdrPlugin.SurvivalT/etc
%{rlibdir}/RcmdrPlugin.SurvivalT/Meta
%{rlibdir}/RcmdrPlugin.SurvivalT/R
%{rlibdir}/RcmdrPlugin.SurvivalT/INDEX
%{rlibdir}/RcmdrPlugin.SurvivalT/help
%{rlibdir}/RcmdrPlugin.SurvivalT/CHANGES

%changelog
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.7-1
- initial package for Fedora