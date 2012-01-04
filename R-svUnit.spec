%global packname  svUnit
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.7.5
Release:          1%{?dist}
Summary:          SciViews GUI API - Unit testing

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.7-5.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
A complete unit test system and functions to implement its GUI part

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
%doc %{rlibdir}/svUnit/NEWS
%doc %{rlibdir}/svUnit/html
%doc %{rlibdir}/svUnit/CITATION
%doc %{rlibdir}/svUnit/doc
%doc %{rlibdir}/svUnit/DESCRIPTION
%{rlibdir}/svUnit/Meta
%{rlibdir}/svUnit/R
%{rlibdir}/svUnit/komodo
%{rlibdir}/svUnit/unitTests
%{rlibdir}/svUnit/INDEX
%{rlibdir}/svUnit/help
%{rlibdir}/svUnit/LICENSE
%{rlibdir}/svUnit/NAMESPACE

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.7.5-1
- initial package for Fedora