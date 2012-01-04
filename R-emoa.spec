%global packname  emoa
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.4.8
Release:          1%{?dist}
Summary:          Evolutionary Multiobjective Optimization Algorithms

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_0.4-8.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Collection of building blocks for the design and analysis of evolutionary
multiobjective optimization algorithms.

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
%doc %{rlibdir}/emoa/DESCRIPTION
%doc %{rlibdir}/emoa/html
%{rlibdir}/emoa/R
%{rlibdir}/emoa/help
%{rlibdir}/emoa/INDEX
%{rlibdir}/emoa/unittests
%{rlibdir}/emoa/libs
%{rlibdir}/emoa/data
%{rlibdir}/emoa/NAMESPACE
%{rlibdir}/emoa/Meta

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.4.8-1
- initial package for Fedora