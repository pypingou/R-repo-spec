%global packname  lmom
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.5
Release:          1%{?dist}
Summary:          L-moments

Group:            Applications/Engineering 
License:          Common Public License Version 1.0
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Functions related to L-moments: computation of L-moments of distributions
and data samples; parameter estimation; L-moment ratio diagram; plot vs.
quantiles of an extreme-value distribution.

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
%doc %{rlibdir}/lmom/CITATION
%doc %{rlibdir}/lmom/DESCRIPTION
%doc %{rlibdir}/lmom/html
%doc %{rlibdir}/lmom/NEWS
%{rlibdir}/lmom/LICENSE
%{rlibdir}/lmom/libs
%{rlibdir}/lmom/Meta
%{rlibdir}/lmom/NAMESPACE
%{rlibdir}/lmom/INDEX
%{rlibdir}/lmom/R
%{rlibdir}/lmom/help

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.5-1
- initial package for Fedora