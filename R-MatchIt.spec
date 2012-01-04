%global packname  MatchIt
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          2.4.20
Release:          1%{?dist}
Summary:          MatchIt

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_2.4-20.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-MASS 

BuildRequires:    R-devel tex(latex) R-MASS 

%description
MatchIt preprocesses data by selecting approximate matched samples of the
treated and control groups with similar covariate distributions, drawing
on a large variety of matching methods.  After preprocessing data with
MatchIt, whatever standard parametric technique one might have used
without preprocessing can be used, but the results will be far less model

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
%doc %{rlibdir}/MatchIt/DESCRIPTION
%doc %{rlibdir}/MatchIt/CITATION
%doc %{rlibdir}/MatchIt/doc
%doc %{rlibdir}/MatchIt/html
%{rlibdir}/MatchIt/NAMESPACE
%{rlibdir}/MatchIt/Meta
%{rlibdir}/MatchIt/demo
%{rlibdir}/MatchIt/help
%{rlibdir}/MatchIt/R
%{rlibdir}/MatchIt/data
%{rlibdir}/MatchIt/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 2.4.20-1
- initial package for Fedora