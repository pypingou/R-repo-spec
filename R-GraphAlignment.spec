%global packname  GraphAlignment
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.16.0
Release:          1%{?dist}
Summary:          GraphAlignment

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Graph alignment is an extension package for the R programming environment
which provides functions for finding an alignment between two networks
based on link and node similarity scores. (J. Berg and M. Laessig,
"Cross-species analysis of biological networks by Bayesian alignment",
PNAS 103 (29), 10967-10972 (2006))

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
%doc %{rlibdir}/GraphAlignment/html
%doc %{rlibdir}/GraphAlignment/DESCRIPTION
%doc %{rlibdir}/GraphAlignment/CITATION
%doc %{rlibdir}/GraphAlignment/doc
%{rlibdir}/GraphAlignment/NAMESPACE
%{rlibdir}/GraphAlignment/help
%{rlibdir}/GraphAlignment/Meta
%{rlibdir}/GraphAlignment/INDEX
%{rlibdir}/GraphAlignment/R
%{rlibdir}/GraphAlignment/libs
%{rlibdir}/GraphAlignment/LICENSE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.16.0-1
- initial package for Fedora