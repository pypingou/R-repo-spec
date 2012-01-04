%global packname  dpmixsim
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.0.7
Release:          1%{?dist}
Summary:          Dirichlet Process Mixture model simulation for clustering and image segmentation

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.0-7.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-oro.nifti R-cluster 


BuildRequires:    R-devel tex(latex) R-oro.nifti R-cluster



%description
The package implements a Dirichlet Process Mixture (DPM) model for
clustering and image segmentation. The DPM model is a Bayesian
nonparametric methodology that relies on MCMC simulations for exploring
mixture models with an unknown number of components. The code implements
conjugate models with normal structure (conjugate normal-normal DP mixture
model). The package's applications are oriented towards the classification
of magnetic resonance images according to tissue type or region of

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
%doc %{rlibdir}/dpmixsim/NEWS
%doc %{rlibdir}/dpmixsim/html
%doc %{rlibdir}/dpmixsim/DESCRIPTION
%{rlibdir}/dpmixsim/libs
%{rlibdir}/dpmixsim/NAMESPACE
%{rlibdir}/dpmixsim/demo
/usr/src/debug/dpmixsim/dpmixsim/src/gibbsclustersamplealpha.cc
%{rlibdir}/dpmixsim/extdata
%{rlibdir}/dpmixsim/INDEX
%{rlibdir}/dpmixsim/data
%{rlibdir}/dpmixsim/help
/usr/lib/debug/.build-id/3a/31b3c7841de6050485084fec16cdf2f237c2a9
/usr/lib/debug/.build-id/3a/31b3c7841de6050485084fec16cdf2f237c2a9.debug
%{rlibdir}/dpmixsim/R
%{rlibdir}/dpmixsim/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.0.7-1
- initial package for Fedora