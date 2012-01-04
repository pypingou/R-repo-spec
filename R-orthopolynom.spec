%global packname  orthopolynom
%global rlibdir  %{_datadir}/R/library


Name:             R-%{packname}
Version:          1.0.3
Release:          1%{?dist}
Summary:          Collection of functions for orthogonal and orthonormal polynomials

Group:            Applications/Engineering 
License:          GPL (>= 2)
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.0-3.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:        noarch
Requires:         R-core

Requires:         R-polynom 

BuildRequires:    R-devel tex(latex) R-polynom 

%description
A collection of functions to construct sets of orthogonal polynomials and
their recurrence relations. Additional functions are provided to calculate
the derivative, integral, value and roots of lists of polynomial objects.

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
%doc %{rlibdir}/orthopolynom/html
%doc %{rlibdir}/orthopolynom/DESCRIPTION
%{rlibdir}/orthopolynom/help
%{rlibdir}/orthopolynom/Meta
%{rlibdir}/orthopolynom/R
%{rlibdir}/orthopolynom/INDEX
%{rlibdir}/orthopolynom/NAMESPACE

%changelog
* Fri Nov 18 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0.3-1
- initial package for Fedora