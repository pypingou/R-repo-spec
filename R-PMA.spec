%global packname  PMA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Penalized Multivariate Analysis

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-plyr 


BuildRequires:    R-devel tex(latex) R-plyr



%description
Performs Penalized Multivariate Analysis: a penalized matrix
decomposition, sparse principal components analysis, and sparse canonical
correlation analysis, described in the following papers: (1) Witten,
Tibshirani and Hastie (2009) A penalized matrix decomposition, with
applications to sparse principal components and canonical correlation
analysis. Biostatistics 10(3):515-534. (2) Witten and Tibshirani (2009)
Extensions of sparse canonical correlation analysis, with applications to
genomic data. Statistical Applications in Genetics and Molecular Biology
8(1): Article 28.

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
* Sat Dec 10 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora