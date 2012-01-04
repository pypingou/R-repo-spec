%global packname  entropy
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.1.6
Release:          1%{?dist}
Summary:          Entropy and Mutual Information Estimation

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package implements various estimators of entropy, such as the
shrinkage estimator by Hausser and Strimmer, the maximum likelihood and
the Millow-Madow estimator, various Bayesian estimators, and the Chao-Shen
estimator.  It also offers an R interface to the NSB estimator.
Furthermore, it provides functions for estimating mutual information.

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
%doc %{rlibdir}/entropy/html
%doc %{rlibdir}/entropy/NEWS
%doc %{rlibdir}/entropy/DESCRIPTION
%{rlibdir}/entropy/R
%{rlibdir}/entropy/NAMESPACE
%{rlibdir}/entropy/help
%{rlibdir}/entropy/Meta
%{rlibdir}/entropy/LICENSE
%{rlibdir}/entropy/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.6-1
- initial package for Fedora