%global packname  editrules
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.9.0
Release:          1%{?dist}
Summary:          R package for parsing and manipulating edit rules

Group:            Applications/Engineering 
License:          GPL-3
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.9-0.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Facilitates reading and manipulating (multivariate) data restrictions
(edit rules) on numerical and categorical data. Rules can be defined with
common R syntax and parsed to an internal (matrix-like format). Rules can
be manipulated with variable elimination and value substitution methods,
allowing for feasibility checks and more. Data can be tested against the
rules and erroneous fields can be found based on Fellegi and Holt's
generalized principle and rules can be visualized with the igraph package.

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
%doc %{rlibdir}/editrules/html
%doc %{rlibdir}/editrules/DESCRIPTION
%doc %{rlibdir}/editrules/NEWS
%doc %{rlibdir}/editrules/doc
%{rlibdir}/editrules/tests
%{rlibdir}/editrules/INDEX
%{rlibdir}/editrules/NAMESPACE
%{rlibdir}/editrules/data
%{rlibdir}/editrules/R
%{rlibdir}/editrules/Meta
%{rlibdir}/editrules/help

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.9.0-1
- initial package for Fedora