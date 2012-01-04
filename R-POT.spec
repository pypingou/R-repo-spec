%global packname  POT
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.1.1
Release:          1%{?dist}
Summary:          Generalized Pareto Distribution and Peaks Over Threshold

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.1-1.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Some functions useful to perform a Peak Over Threshold analysis in
univariate and bivariate cases. A user's guide is avalaible.

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
%doc %{rlibdir}/POT/DESCRIPTION
%doc %{rlibdir}/POT/html
%doc %{rlibdir}/POT/doc
%{rlibdir}/POT/demo
%{rlibdir}/POT/NAMESPACE
%{rlibdir}/POT/INDEX
%{rlibdir}/POT/ChangeLog
%{rlibdir}/POT/Meta
%{rlibdir}/POT/help
%{rlibdir}/POT/CHANGES
%{rlibdir}/POT/libs
%{rlibdir}/POT/R
%{rlibdir}/POT/data

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.1.1-1
- initial package for Fedora