%global packname  multic
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.3.2
Release:          1%{?dist}
Summary:          Quantitative linkage analysis tools using the variance components approach

Group:            Applications/Engineering 
License:          GPL (>= 2) | file LICENSE
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
 Calculate the polygenic and major gene models for quantitative trait
linkage analysis using variance components approach.  The 0.2.2 release
includes bug fixes that allow multic to run properly on 64-bit systems. 
The 0.3.0 release includes a fully implemented sw2mloci function.  Note to
Splus users:  sw2mloci requires Splus 8 or greater.

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
%doc %{rlibdir}/multic/DESCRIPTION
%doc %{rlibdir}/multic/html
%{rlibdir}/multic/R
%{rlibdir}/multic/libs
%{rlibdir}/multic/INDEX
%{rlibdir}/multic/LICENSE
%{rlibdir}/multic/NAMESPACE
%{rlibdir}/multic/Meta
%{rlibdir}/multic/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.3.2-1
- initial package for Fedora