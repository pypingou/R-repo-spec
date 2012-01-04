%global packname  Oncotree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.1
Release:          1%{?dist}
Summary:          Estimating oncogenetic trees

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-boot 

BuildRequires:    R-devel tex(latex) R-boot 

%description
Contains functions to construct and evaluate directed tree structures that
model the process of occurrence of genetic alterations during

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
%doc %{rlibdir}/Oncotree/html
%doc %{rlibdir}/Oncotree/DESCRIPTION
%doc %{rlibdir}/Oncotree/doc
%{rlibdir}/Oncotree/NAMESPACE
%{rlibdir}/Oncotree/help
%{rlibdir}/Oncotree/INDEX
%{rlibdir}/Oncotree/data
%{rlibdir}/Oncotree/R
%{rlibdir}/Oncotree/Meta

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.1-1
- initial package for Fedora