%global packname  regress
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.2
Release:          1%{?dist}
Summary:          Gaussian linear models with linear covariance structure

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
Functions to fit Gaussian linear model by maximising the residual log
likelihood where the covariance structure can be written as a linear
combination of known matrices.  Can be used for multivariate models and
random effects models.  Easy straight forward manner to specify random
effects models, including random interactions. Code now optimised to use
Sherman Woodley identities for matrix inversion in random effects models.

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
%doc %{rlibdir}/regress/DESCRIPTION
%doc %{rlibdir}/regress/html
%{rlibdir}/regress/R
%{rlibdir}/regress/NAMESPACE
%{rlibdir}/regress/help
%{rlibdir}/regress/INDEX
%{rlibdir}/regress/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2-1
- initial package for Fedora