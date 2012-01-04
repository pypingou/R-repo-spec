%global packname  DEoptim
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.1.1
Release:          1%{?dist}
Summary:          Global optimization by differential evolution

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
This package provides the DEoptim function which performs global
optimization by differential evolution.

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
%doc %{rlibdir}/DEoptim/NEWS
%doc %{rlibdir}/DEoptim/CITATION
%doc %{rlibdir}/DEoptim/DESCRIPTION
%doc %{rlibdir}/DEoptim/doc
%doc %{rlibdir}/DEoptim/html
%{rlibdir}/DEoptim/data
%{rlibdir}/DEoptim/INDEX
%{rlibdir}/DEoptim/Meta
%{rlibdir}/DEoptim/help
%{rlibdir}/DEoptim/NAMESPACE
%{rlibdir}/DEoptim/R
%{rlibdir}/DEoptim/demo
%{rlibdir}/DEoptim/libs

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.1.1-1
- initial package for Fedora