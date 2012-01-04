%global packname  dynaTree
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.2.2
Release:          1%{?dist}
Summary:          Dynamic trees for learning and design

Group:            Applications/Engineering 
License:          LGPL
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_1.2-2.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:         R-methods 

BuildRequires:    R-devel tex(latex) R-methods 

%description
Inference by sequential Monte Carlo for dynamic tree regression and
classification models with hooks provided for sequential design and
optimization, fully online learning with drift, variable selection, and
sensitivity analysis of inputs. Illustrative examples from the original
dynamic trees paper are facilitated by demos in the package; see

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
%doc %{rlibdir}/dynaTree/html
%doc %{rlibdir}/dynaTree/DESCRIPTION
%{rlibdir}/dynaTree/data
%{rlibdir}/dynaTree/R
%{rlibdir}/dynaTree/NAMESPACE
%{rlibdir}/dynaTree/libs
%{rlibdir}/dynaTree/Meta
%{rlibdir}/dynaTree/demo
RPM build errors:
%{rlibdir}/dynaTree/LICENSE
%{rlibdir}/dynaTree/help
%{rlibdir}/dynaTree/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.2.2-1
- initial package for Fedora