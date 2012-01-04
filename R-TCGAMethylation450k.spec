%global packname  TCGAMethylation450k
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          0.99.1
Release:          1%{?dist}
Summary:          The Cancer Genome Atlas Illumina 450k methylation example data

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/data/experiment/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/experiment/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core



BuildRequires:    R-devel tex(latex)  

%description
The Cancer Genome Atlas (TCGA) is applying genomics technologies to over
20 different types of cancer.  This package contains a small set of 450k
array data in idat format.

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
%doc %{rlibdir}/TCGAMethylation450k/html
%doc %{rlibdir}/TCGAMethylation450k/DESCRIPTION
%{rlibdir}/TCGAMethylation450k/help
%{rlibdir}/TCGAMethylation450k/extdata
%{rlibdir}/TCGAMethylation450k/Meta
%{rlibdir}/TCGAMethylation450k/INDEX
%{rlibdir}/TCGAMethylation450k/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.1-1
- initial package for Fedora