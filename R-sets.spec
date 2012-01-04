%global packname  sets
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.8
Release:          1%{?dist}
Summary:          Sets, Generalized Sets, Customizable Sets and Intervals

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Data structures and basic operations for ordinary sets, generalizations
such as fuzzy sets, multisets, and fuzzy multisets, customizable sets, and

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
%doc %{rlibdir}/sets/doc
%doc %{rlibdir}/sets/DESCRIPTION
%doc %{rlibdir}/sets/CITATION
%doc %{rlibdir}/sets/html
%{rlibdir}/sets/R
%{rlibdir}/sets/NEWS.Rd
%{rlibdir}/sets/libs
%{rlibdir}/sets/NAMESPACE
%{rlibdir}/sets/Meta
%{rlibdir}/sets/data
%{rlibdir}/sets/help
%{rlibdir}/sets/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.8-1
- initial package for Fedora