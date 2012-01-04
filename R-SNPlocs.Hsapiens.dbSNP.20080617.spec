%global packname  SNPlocs.Hsapiens.dbSNP.20080617
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.99.1
Release:          1%{?dist}
Summary:          SNP locations for Homo sapiens

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/data/annotation/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/data/annotation/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
SNP locations and alleles for Homo sapiens extracted from dbSNP. The
source data files used for this package were created by NCBI on 17-18 June
2008. This package can be used for SNP injection into the
BSgenome.Hsapiens.UCSC.hg18 package.

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
%doc %{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/html
%doc %{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/DESCRIPTION
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/NAMESPACE
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/help
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/R
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/data
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/Meta
%{rlibdir}/SNPlocs.Hsapiens.dbSNP.20080617/tools

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.99.1-1
- initial package for Fedora