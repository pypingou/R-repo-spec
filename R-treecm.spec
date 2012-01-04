%global packname  treecm
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.2
Release:          1%{?dist}
Summary:          Estimating and plotting the centre of mass of a tree.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Given a few data about branchiness of a tree the package computes and
plots the centre of mass of the tree itself. The centre of mass is a
crucial data for arborists in order to consolidate a tree using steel or
dynamic cables. Slenderness ratio of branches may also be assessed and
plot in order to aid the pruning selection process

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
%doc %{rlibdir}/treecm/doc
%doc %{rlibdir}/treecm/DESCRIPTION
%doc %{rlibdir}/treecm/html
%{rlibdir}/treecm/Meta
%{rlibdir}/treecm/NAMESPACE
%{rlibdir}/treecm/R
%{rlibdir}/treecm/help
%{rlibdir}/treecm/INDEX
%{rlibdir}/treecm/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.2-1
- initial package for Fedora