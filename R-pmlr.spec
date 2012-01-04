%global packname  pmlr
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Penalized Multinomial Logistic Regression

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Extends the approach proposed by Firth (1993) for bias reduction of MLEs
in exponential family models to the multinomial logistic regression model
with general covariate types.  Modification of the logistic regression
score function to remove first-order bias is equivalent to penalizing the
likelihood by the Jeffreys prior, and yields penalized maximum likelihood
estimates (PLEs) that always exist.  Hypothesis testing is conducted via
likelihood ratio statistics.  Profile confidence intervals (CI) are
constructed for the PLEs.

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
%doc %{rlibdir}/pmlr/DESCRIPTION
%doc %{rlibdir}/pmlr/html
%{rlibdir}/pmlr/Meta
%{rlibdir}/pmlr/data
%{rlibdir}/pmlr/help
%{rlibdir}/pmlr/INDEX
%{rlibdir}/pmlr/R
%{rlibdir}/pmlr/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora