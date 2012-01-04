%global packname  kernlab
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.9.14
Release:          1%{?dist}
Summary:          Kernel-based Machine Learning Lab

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.9-14.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Kernel-based machine learning methods for classification, regression,
clustering, novelty detection, quantile regression and dimensionality
reduction. Among other methods kernlab includes Support Vector Machines,
Spectral Clustering, Kernel PCA and a QP solver.

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
%doc %{rlibdir}/kernlab/DESCRIPTION
%doc %{rlibdir}/kernlab/CITATION
%doc %{rlibdir}/kernlab/doc
%doc %{rlibdir}/kernlab/html
%{rlibdir}/kernlab/data
%{rlibdir}/kernlab/libs
%{rlibdir}/kernlab/Meta
%{rlibdir}/kernlab/R
%{rlibdir}/kernlab/NAMESPACE
%{rlibdir}/kernlab/INDEX
%{rlibdir}/kernlab/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.9.14-1
- initial package for Fedora