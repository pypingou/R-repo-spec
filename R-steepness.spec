%global packname  steepness
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          0.2
Release:          1%{?dist}
Summary:          Testing Steepness of Dominance Hierarchies

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
steepness is a package that computes steepness as a property of dominance
hierarchies. Steepness is defined as the absolute slope of the straight
line fitted to the normalized David's scores. The normalized David's
scores can be obtained on the basis of dyadic dominance indices corrected
for chance or by means of proportions of wins. Given an observed
sociomatrix, it computes hierarchy's steepness and estimates statistical
significance by means of a randomization test.

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
%doc %{rlibdir}/steepness/NEWS
%doc %{rlibdir}/steepness/html
%doc %{rlibdir}/steepness/DESCRIPTION
%{rlibdir}/steepness/help
%{rlibdir}/steepness/Meta
%{rlibdir}/steepness/libs
%{rlibdir}/steepness/NAMESPACE
%{rlibdir}/steepness/R
%{rlibdir}/steepness/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 0.2-1
- initial package for Fedora