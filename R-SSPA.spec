%global packname  SSPA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.10.0
Release:          1%{?dist}
Summary:          Sample Size and Power Analysis for Microarray Data

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-qvalue 
Requires:         R-graphics R-limma R-methods R-stats 

BuildRequires:    R-devel tex(latex) R-methods R-qvalue
BuildRequires:    R-graphics R-limma R-methods R-stats 


%description
Sample size and power analysis for microarray data, where two groups are

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
%doc %{rlibdir}/SSPA/doc
%doc %{rlibdir}/SSPA/CITATION
%doc %{rlibdir}/SSPA/DESCRIPTION
%doc %{rlibdir}/SSPA/NEWS
%doc %{rlibdir}/SSPA/html
%{rlibdir}/SSPA/R
%{rlibdir}/SSPA/NAMESPACE
%{rlibdir}/SSPA/help
%{rlibdir}/SSPA/INDEX
%{rlibdir}/SSPA/Meta

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.10.0-1
- initial package for Fedora