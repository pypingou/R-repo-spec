%global packname  CoCoCg
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.1.7.6
Release:          1%{?dist}
Summary:          Graphical modelling by CG regressions

Group:            Applications/Engineering 
License:          file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods R-CoCo 


BuildRequires:    R-devel tex(latex) R-methods R-CoCo



%description
Interface to CoCoCg (CoCo with both discrete and continuous data) from R.

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
%doc %{rlibdir}/CoCoCg/html
%doc %{rlibdir}/CoCoCg/DESCRIPTION
%{rlibdir}/CoCoCg/CreateDatasets
%{rlibdir}/CoCoCg/LICENSE
%{rlibdir}/CoCoCg/libs
%{rlibdir}/CoCoCg/INDEX
%{rlibdir}/CoCoCg/help
%{rlibdir}/CoCoCg/Meta
%{rlibdir}/CoCoCg/demo
%{rlibdir}/CoCoCg/data
%{rlibdir}/CoCoCg/NAMESPACE
%{rlibdir}/CoCoCg/R

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.1.7.6-1
- initial package for Fedora