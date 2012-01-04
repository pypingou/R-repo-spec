%global packname  ibdreg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.3
Release:          1%{?dist}
Summary:          Regression Methods for IBD Linkage With Covariates

Group:            Applications/Engineering 
License:          GPL-2 | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A method to test genetic linkage with covariates by regression methods
with response IBD sharing for relative pairs.  Account for correlations of
IBD statistics and covariates for relative pairs within the same pedigree.

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
%doc %{rlibdir}/ibdreg/html
%doc %{rlibdir}/ibdreg/DESCRIPTION
%doc %{rlibdir}/ibdreg/doc
%{rlibdir}/ibdreg/help
%{rlibdir}/ibdreg/R
%{rlibdir}/ibdreg/INDEX
%{rlibdir}/ibdreg/LICENSE
%{rlibdir}/ibdreg/NAMESPACE
%{rlibdir}/ibdreg/libs
%{rlibdir}/ibdreg/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.3-1
- initial package for Fedora