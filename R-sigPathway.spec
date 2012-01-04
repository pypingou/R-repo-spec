%global packname  sigPathway
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.22.0
Release:          1%{?dist}
Summary:          Pathway Analysis

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Conducts pathway analysis by calculating the NT_k and NE_k statistics as
described in Tian et al. (2005)

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
%doc %{rlibdir}/sigPathway/DESCRIPTION
%doc %{rlibdir}/sigPathway/doc
%doc %{rlibdir}/sigPathway/html
%{rlibdir}/sigPathway/R
%{rlibdir}/sigPathway/INDEX
%{rlibdir}/sigPathway/NAMESPACE
%{rlibdir}/sigPathway/help
%{rlibdir}/sigPathway/Meta
%{rlibdir}/sigPathway/data
%{rlibdir}/sigPathway/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.22.0-1
- initial package for Fedora