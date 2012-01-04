%global packname  SPIA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.0
Release:          1%{?dist}
Summary:          Signaling Pathway Impact Analysis (SPIA) using combined evidence of pathway over-representation and unusual signaling perturbations

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-graphics 

BuildRequires:    R-devel tex(latex) R-graphics 

%description
This package implements the Signaling Pathway Impact Analysis (SPIA) which
uses the information form a list of differentially expressed genes and
their log fold changes together with signaling pathways topology, in order
to identify the pathways most relevant to the condition under the study.

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
%doc %{rlibdir}/SPIA/doc
%doc %{rlibdir}/SPIA/DESCRIPTION
%doc %{rlibdir}/SPIA/html
%{rlibdir}/SPIA/help
%{rlibdir}/SPIA/INDEX
%{rlibdir}/SPIA/Meta
%{rlibdir}/SPIA/NAMESPACE
RPM build errors:
%{rlibdir}/SPIA/extdata
%{rlibdir}/SPIA/R
%{rlibdir}/SPIA/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.0-1
- initial package for Fedora