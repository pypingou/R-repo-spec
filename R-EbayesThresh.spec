%global packname  EbayesThresh
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.3.2
Release:          1%{?dist}
Summary:          Empirical Bayes Thresholding and Related Methods

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
This package carries out Empirical Bayes thresholding using the methods
developed by I. M. Johnstone and B. W. Silverman. The basic problem is to
estimate a mean vector given a vector of observations of the mean vector
plus white noise, taking advantage of possible sparsity in the mean
vector. Within a Bayesian formulation, the elements of the mean vector are
modelled as having, independently, a distribution that is a mixture of an
atom of probability at zero and a suitable heavy-tailed distribution.  The
mixing parameter can be estimated by a marginal maximum likelihood
approach.  This leads to an adaptive thresholding approach on the original
data.  Extensions of the basic method, in particular to wavelet
thresholding, are also implemented within the package.

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
%doc %{rlibdir}/EbayesThresh/html
%doc %{rlibdir}/EbayesThresh/DESCRIPTION
%{rlibdir}/EbayesThresh/INDEX
%{rlibdir}/EbayesThresh/R
%{rlibdir}/EbayesThresh/NAMESPACE
%{rlibdir}/EbayesThresh/help
%{rlibdir}/EbayesThresh/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.3.2-1
- initial package for Fedora