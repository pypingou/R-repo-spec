%global packname  risksetROC
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Riskset ROC curve estimation from censored survival data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-survival 

BuildRequires:    R-devel tex(latex) R-survival 

%description
Compute time-dependent Incident/dynamic accuracy measures (ROC curve, AUC,
integrated AUC )from censored survival data under proportional or
non-proportional hazard assumption of Heagerty & Zheng (Biometrics, Vol 61
No 1, 2005, PP 92-105).

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
%doc %{rlibdir}/risksetROC/DESCRIPTION
%doc %{rlibdir}/risksetROC/html
%{rlibdir}/risksetROC/R
%{rlibdir}/risksetROC/NAMESPACE
%{rlibdir}/risksetROC/help
%{rlibdir}/risksetROC/INDEX
%{rlibdir}/risksetROC/Meta
%{rlibdir}/risksetROC/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora