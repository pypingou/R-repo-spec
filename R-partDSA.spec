%global packname  partDSA
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.1
Release:          1%{?dist}
Summary:          Partitioning using deletion, substitution, and addition moves

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
partDSA is a novel tool for generating a piecewise constant estimation
list of increasingly complex predictors based on an intensive and
comprehensive search over the entire covariate space.

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
%doc %{rlibdir}/partDSA/DESCRIPTION
%doc %{rlibdir}/partDSA/doc
%doc %{rlibdir}/partDSA/html
%{rlibdir}/partDSA/java
%{rlibdir}/partDSA/Meta
%{rlibdir}/partDSA/R
%{rlibdir}/partDSA/examples
%{rlibdir}/partDSA/NAMESPACE
%{rlibdir}/partDSA/INDEX
%{rlibdir}/partDSA/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.1-1
- initial package for Fedora