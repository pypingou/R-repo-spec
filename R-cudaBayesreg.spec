%global packname  cudaBayesreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.13
Release:          1%{?dist}
Summary:          CUDA Parallel Implementation of a Bayesian Multilevel Model for fMRI Data Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.3-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cudaBayesregData R-oro.nifti 


BuildRequires:    R-devel tex(latex) R-cudaBayesregData R-oro.nifti



%description
Compute Unified Device Architecture (CUDA) is a software platform for
massively parallel high-performance computing on NVIDIA GPUs. This package
provides a CUDA implementation of a Bayesian multilevel model for the
analysis of brain fMRI data. A fMRI data set consists of time series of
volume data in 4D space. Typically, volumes are collected as slices of 64
x 64 voxels. Analysis of fMRI data often relies on fitting linear
regression models at each voxel of the brain. The volume of the data to be
processed, and the type of statistical analysis to perform in fMRI
analysis, call for high-performance computing strategies. In this package,
the CUDA programming model uses a separate thread for fitting a linear
regression model at each voxel in parallel. The global statistical model
implements a Gibbs Sampler for hierarchical linear models with a normal
prior. This model has been proposed by Rossi, Allenby and McCulloch in
`Bayesian Statistics and Marketing', Chapter 3, and is referred to as
`rhierLinearModel' in the R-package bayesm. A notebook equipped with a
NVIDIA `GeForce 8400M GS' card having Compute Capability 1.1 has been used
in the tests. The data sets used in the package's examples are available
in the separate package cudaBayesregData.

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
%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.13-1
- initial package for Fedora