%global packname  LMGene
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.10.0
Release:          1%{?dist}
Summary:          LMGene Software for Data Transformation and Identification of Differentially Expressed Genes in Gene Expression Arrays

Group:            Applications/Engineering 
License:          LGPL
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase R-multtest R-survival R-affy 


BuildRequires:    R-devel tex(latex) R-Biobase R-multtest R-survival R-affy



%description
LMGene package for analysis of microarray data using a linear model and
glog data transformation

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
* Fri Dec 09 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.10.0-1
- initial package for Fedora