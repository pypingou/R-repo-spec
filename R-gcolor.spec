%global packname  gcolor
%global rlibdir  %{_libdir}/R/library


Name:             R-%{packname}
Version:          1.0
Release:          1%{?dist}
Summary:          Provides an Inequation Algorithm Function and a solution to import DIMACS files.

Group:            Applications/Engineering 
License:          GPL-2
URL:              http://cran.r-project.org/web/packages/%{packname}/index.html
Source0:          http://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz
BuildRoot:        %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)



BuildRequires:    R-devel tex(latex)  

%description
Generates a valid colouring of a graph by solving the system of
inequations representing the graph.

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
%doc %{rlibdir}/gcolor/DESCRIPTION
%doc %{rlibdir}/gcolor/html
%{rlibdir}/gcolor/generalized_decision_function.pdf
%{rlibdir}/gcolor/NAMESPACE
%{rlibdir}/gcolor/help
%{rlibdir}/gcolor/libs
%{rlibdir}/gcolor/systems_of_inequations.pdf
%{rlibdir}/gcolor/Meta
%{rlibdir}/gcolor/statistical_characterization_np.pdf
%{rlibdir}/gcolor/R
%{rlibdir}/gcolor/optimal_solution_constraint.pdf
%{rlibdir}/gcolor/equivalence_class_subset_algorithm.pdf
%{rlibdir}/gcolor/gcolor.pdf
%{rlibdir}/gcolor/INDEX

%changelog
* Thu Nov 17 2011 Pierre-Yves Chibon <pingou@pingoured.fr> 1.0-1
- initial package for Fedora