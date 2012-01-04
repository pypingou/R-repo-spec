%global packname  mdqc
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          Mahalanobis Distance Quality Control for microarrays

Group:            Applications/Engineering 
License:          LGPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-cluster R-MASS 

BuildRequires:    R-devel tex(latex) R-cluster R-MASS 

%description
MDQC is a multivariate quality assessment method for microarrays based on
quality control (QC) reports. The Mahalanobis distance of an array's
quality attributes is used to measure the similarity of the quality of
that array against the quality of the other arrays. Then, arrays with
unusually high distances can be flagged as potentially low-quality.

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
%doc %{rlibdir}/mdqc/doc
%doc %{rlibdir}/mdqc/DESCRIPTION
%doc %{rlibdir}/mdqc/html
%{rlibdir}/mdqc/NAMESPACE
%{rlibdir}/mdqc/R
%{rlibdir}/mdqc/data
%{rlibdir}/mdqc/help
%{rlibdir}/mdqc/INDEX
%{rlibdir}/mdqc/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora