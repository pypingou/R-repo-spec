%global packname  PearsonDS
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.92
Release:          1%{?dist}
Summary:          Pearson Distribution System

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Implementation of the Pearson distribution system, including full support
for the (d,p,q,r)-family of functions for probability distributions and
fitting via method of moments and maximum likelihood method.

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
%doc %{rlibdir}/PearsonDS/html
%doc %{rlibdir}/PearsonDS/DESCRIPTION
%doc %{rlibdir}/PearsonDS/CITATION
%{rlibdir}/PearsonDS/INDEX
%{rlibdir}/PearsonDS/CHANGES
%{rlibdir}/PearsonDS/NAMESPACE
%{rlibdir}/PearsonDS/help
%{rlibdir}/PearsonDS/R
%{rlibdir}/PearsonDS/libs
%{rlibdir}/PearsonDS/Meta
%{rlibdir}/PearsonDS/LICENSE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.92-1
- initial package for Fedora