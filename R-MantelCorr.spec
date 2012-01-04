%global packname  MantelCorr
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.24.0
Release:          1%{?dist}
Summary:          Compute Mantel Cluster Correlations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Computes Mantel cluster correlations from a (p x n) numeric data matrix
(e.g. microarray gene-expression data).

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
%doc %{rlibdir}/MantelCorr/DESCRIPTION
%doc %{rlibdir}/MantelCorr/html
%doc %{rlibdir}/MantelCorr/doc
%{rlibdir}/MantelCorr/Meta
%{rlibdir}/MantelCorr/data
%{rlibdir}/MantelCorr/R
%{rlibdir}/MantelCorr/NAMESPACE
%{rlibdir}/MantelCorr/help
%{rlibdir}/MantelCorr/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.24.0-1
- initial package for Fedora