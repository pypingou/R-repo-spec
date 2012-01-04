%global packname  gmm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.3.8
Release:          1%{?dist}
Summary:          Generalized Method of Moments and Generalized Empirical Likelihood

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.3-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-sandwich 

BuildRequires:    R-devel tex(latex) R-sandwich 

%description
It is a complete suite to estimate models based on moment conditions. It
includes the two step Generalized method of moments (GMM) of Hansen(1982),
the iterated GMM and continuous updated estimator (CUE) of
Hansen-Eaton-Yaron(1996) and several methods that belong to the
Generalized Empirical Likelihood (GEL) family of estimators, as presented
by Smith(1997), Kitamura(1997), Newey-Smith(2004) and Anatolyev(2005).

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
%doc %{rlibdir}/gmm/NEWS
%doc %{rlibdir}/gmm/html
%doc %{rlibdir}/gmm/DESCRIPTION
%doc %{rlibdir}/gmm/doc
%doc %{rlibdir}/gmm/CITATION
%{rlibdir}/gmm/R
%{rlibdir}/gmm/Meta
%{rlibdir}/gmm/data
%{rlibdir}/gmm/INDEX
%{rlibdir}/gmm/help
%{rlibdir}/gmm/NAMESPACE

%changelog
* Fri Nov 25 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.8-1
- initial package for Fedora