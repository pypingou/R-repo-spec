%global packname  SpeCond
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.8.0
Release:          1%{?dist}
Summary:          Condition specific detection from expression data

Group:            Applications/Engineering 
License:          LGPL (>=2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-mclust R-Biobase R-fields R-hwriter R-RColorBrewer R-methods 

BuildRequires:    R-devel tex(latex) R-mclust R-Biobase R-fields R-hwriter R-RColorBrewer R-methods 

%description
This package performs a gene expression data analysis to detect
condition-specific genes. Such genes are significantly up- or
down-regulated in a small number of conditions. It does so by fitting a
mixture of normal distributions to the expression values. Conditions can
be environmental conditions, different tissues, organs or any other
sources that you wish to compare in terms of gene expression.

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
* Thu Nov 24 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.8.0-1
- initial package for Fedora