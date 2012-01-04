%global packname  BiocCaseStudies
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          BiocCaseStudies: Support for the Case Studies Monograph

Group:            Applications/Engineering 
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-tools R-methods R-utils R-Biobase 

BuildRequires:    R-devel tex(latex) R-tools R-methods R-utils R-Biobase 

%description
Software and data to support the case studies.

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
%doc %{rlibdir}/BiocCaseStudies/html
%doc %{rlibdir}/BiocCaseStudies/DESCRIPTION
%{rlibdir}/BiocCaseStudies/help
%{rlibdir}/BiocCaseStudies/R
%{rlibdir}/BiocCaseStudies/NAMESPACE
%{rlibdir}/BiocCaseStudies/INDEX
%{rlibdir}/BiocCaseStudies/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora