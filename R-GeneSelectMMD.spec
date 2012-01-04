%global packname  GeneSelectMMD
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Gene selection based on the marginal distributions of gene profiles that characterized by a mixture of three-component multivariate distributions

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-Biobase 
Requires:         R-Biobase R-MASS R-graphics R-stats R-survival R-limma 

BuildRequires:    R-devel tex(latex) R-Biobase
BuildRequires:    R-Biobase R-MASS R-graphics R-stats R-survival R-limma 


%description
Gene selection based on a mixture of marginal distributions

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
%doc %{rlibdir}/GeneSelectMMD/doc
%doc %{rlibdir}/GeneSelectMMD/DESCRIPTION
%doc %{rlibdir}/GeneSelectMMD/html
%{rlibdir}/GeneSelectMMD/Meta
%{rlibdir}/GeneSelectMMD/NAMESPACE
%{rlibdir}/GeneSelectMMD/help
%{rlibdir}/GeneSelectMMD/INDEX
%{rlibdir}/GeneSelectMMD/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora