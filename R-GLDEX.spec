%global packname  GLDEX
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.4.1
Release:          1%{?dist}
Summary:          Fitting Single and Mixture of Generalised Lambda Distributions (RS and FMKL) using Various Methods

Group:            Applications/Engineering 
License:          GPL (>= 3)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster 

BuildRequires:    R-devel tex(latex) R-cluster 

%description
The fitting algorithms considered in this package have two major
objectives. One is to provide a smoothing device to fit distributions to
data using the weight and unweighted discretised approach based on the bin
width of the histogram. The other is to provide a definitive fit to the
data set using the maximum likelihood and quantile matching estimation.
Other methods such as moment matching, starship method, L moment matching
are also provided. Diagnostics on goodness of fit can be done via qqplots,
KS-resample tests and comparing mean, variance, skewness and kurtosis of
the data with the fitted distribution.

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
%doc %{rlibdir}/GLDEX/DESCRIPTION
%doc %{rlibdir}/GLDEX/html
%{rlibdir}/GLDEX/NAMESPACE
%{rlibdir}/GLDEX/Meta
%{rlibdir}/GLDEX/INDEX
%{rlibdir}/GLDEX/R
%{rlibdir}/GLDEX/libs
%{rlibdir}/GLDEX/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.4.1-1
- initial package for Fedora