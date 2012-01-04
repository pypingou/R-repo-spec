%global packname  SLqPCR
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.20.0
Release:          1%{?dist}
Summary:          Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions for analysis of real-time quantitative PCR data at SIRS-Lab GmbH

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
%doc %{rlibdir}/SLqPCR/doc
%doc %{rlibdir}/SLqPCR/CITATION
%doc %{rlibdir}/SLqPCR/DESCRIPTION
%doc %{rlibdir}/SLqPCR/html
%{rlibdir}/SLqPCR/INDEX
%{rlibdir}/SLqPCR/Meta
%{rlibdir}/SLqPCR/help
%{rlibdir}/SLqPCR/NAMESPACE
%{rlibdir}/SLqPCR/R
%{rlibdir}/SLqPCR/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.20.0-1
- initial package for Fedora