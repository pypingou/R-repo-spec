%global packname  mlmRev
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0.1
Release:          1%{?dist}
Summary:          Examples from Multilevel Modelling Software Review

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-lme4 


BuildRequires:    R-devel tex(latex) R-lme4



%description
Data and examples from a multilevel modelling software review as well as
other well-known data sets from the multilevel modelling literature.

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
%doc %{rlibdir}/mlmRev/html
%doc %{rlibdir}/mlmRev/DESCRIPTION
%doc %{rlibdir}/mlmRev/doc
%{rlibdir}/mlmRev/data
%{rlibdir}/mlmRev/help
%{rlibdir}/mlmRev/Meta
%{rlibdir}/mlmRev/INDEX
%{rlibdir}/mlmRev/NAMESPACE
%{rlibdir}/mlmRev/original

%changelog
* Thu Dec 08 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.1-1
- initial package for Fedora