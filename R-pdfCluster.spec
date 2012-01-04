%global packname  pdfCluster
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.13
Release:          1%{?dist}
Summary:          Cluster analysis via nonparametric density estimation

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.1-13.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-geometry 

BuildRequires:    R-devel tex(latex) R-methods R-geometry 

%description
The package performs cluster analysis via kernel density estimation.
Clusters are associated to the maximally connected components with
estimated density above a threshold. Diagnostics methods for evaluating
the quality of clustering are also available.  The package includes also a
routine to estimate the probability density function by the kernel method,
given a set of data with arbitrary dimensions.

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
%doc %{rlibdir}/pdfCluster/html
%doc %{rlibdir}/pdfCluster/DESCRIPTION
%doc %{rlibdir}/pdfCluster/CITATION
%{rlibdir}/pdfCluster/Meta
%{rlibdir}/pdfCluster/help
%{rlibdir}/pdfCluster/libs
%{rlibdir}/pdfCluster/R
%{rlibdir}/pdfCluster/INDEX
RPM build errors:
%{rlibdir}/pdfCluster/data
%{rlibdir}/pdfCluster/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.13-1
- initial package for Fedora