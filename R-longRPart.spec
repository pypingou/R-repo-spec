%global packname  longRPart
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Recursive partitioning of longitudinal data using mixed-effects models

Group:            Applications/Engineering 
License:          GPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-nlme R-rpart 

BuildRequires:    R-devel tex(latex) R-nlme R-rpart 

%description


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
%doc %{rlibdir}/longRPart/doc
%doc %{rlibdir}/longRPart/DESCRIPTION
%doc %{rlibdir}/longRPart/html
%{rlibdir}/longRPart/Meta
%{rlibdir}/longRPart/INDEX
%{rlibdir}/longRPart/NAMESPACE
%{rlibdir}/longRPart/help
%{rlibdir}/longRPart/data
%{rlibdir}/longRPart/R

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora