%global packname  SPIAssay
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.0
Release:          1%{?dist}
Summary:          A genetic-based assay for the identification of cell lines

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The SNP Panel Identification Assay (SPIA) is a package that enables an
accurate determination of cell line identity from the genotype of single
nucleotide polymorphisms (SNPs). The SPIA test allows to discern when two
cell lines are close enough to be called similar and when they are not.

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
%doc %{rlibdir}/SPIAssay/DESCRIPTION
%doc %{rlibdir}/SPIAssay/html
%{rlibdir}/SPIAssay/R
%{rlibdir}/SPIAssay/NAMESPACE
%{rlibdir}/SPIAssay/help
%{rlibdir}/SPIAssay/INDEX
%{rlibdir}/SPIAssay/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.0-1
- initial package for Fedora